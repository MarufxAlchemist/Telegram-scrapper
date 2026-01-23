from telethon import TelegramClient, errors
import pandas as pd
from datetime import datetime as dt
from time import sleep
import os
import asyncio

class TelegramChannelScraper:
    def __init__(self):
        self.credentials = {}
        
        # Try to load from environment variables first
        api_id = os.getenv('TELEGRAM_API_ID')
        api_hash = os.getenv('TELEGRAM_API_HASH')
        phone = os.getenv('TELEGRAM_PHONE')

        if api_id and api_hash and phone:
            self.credentials["api_id"] = api_id.strip()
            self.credentials["api_hash"] = api_hash.strip()
            self.credentials["phone"] = phone.strip()
            print(f"\nLoaded credentials from environment variables for phone: {self.credentials['phone']}\n")
        else:
            credentials_provided = False
            while not credentials_provided:
                self.credentials["api_id"] = input("\nProvide your Telegram api_id:\n(Shift + insert to paste)\n").strip()
                self.credentials["api_hash"] = input("\nProvide your Telegram api_hash:\n(Shift + insert to paste)\n").strip()
                self.credentials["phone"] = input("\nProvide your Telegram account phone number (in +123456789 format):\n(Shift + insert to paste)\n").strip()
                print(f"\nThese are the credentials you provided:\n{self.credentials}\n")
                user_accepts = input(
                    "\nDo you wish to proceed? Enter 'y' to continue or 'n' to start over:\n")

                if user_accepts.strip().lower() == 'y':
                    credentials_provided = True

    async def start_client(self):
        self.client = TelegramClient(
            "", 
            self.credentials["api_id"], 
            self.credentials["api_hash"],
        )
        print("\n------------------------------\n")
        print("Client initialized\n")
        await self.authenticate()

    async def authenticate(self):
        await self.client.connect()
        print("Client connected\n")

        is_auth = await self.client.is_user_authorized()
        if not is_auth:
            print("Not authenticated; signing in\n")
            try:
                await self.client.send_code_request(self.credentials["phone"])
                code = input("Enter the code you received:\n").strip()
                await self.client.sign_in(self.credentials["phone"], code)
                print("\nClient authenticated\n\n")
            except errors.SessionPasswordNeededError:
                password = input("Two-Step Verification is enabled. Please enter your password:\n").strip()
                await self.client.sign_in(password=password)
                print("\nClient authenticated with password\n\n")
            except errors.PhoneNumberInvalidError:
                print("The phone number provided is invalid. Please check and try again.")
                await self.client.disconnect()
                exit(1)
            except errors.PhoneCodeInvalidError:
                print("The code entered is invalid. Please try again.")
                await self.client.disconnect()
                exit(1)
            except Exception as e:
                print(f"An unexpected error occurred during authentication: {e}")
                await self.client.disconnect()
                exit(1)

    async def get_messages(self):
        self.today_date = dt.today().strftime("%Y-%m-%d")
        self.target_channel = None

        channel_provided = False
        while not channel_provided:
            print("\n------------------------------\n")
            entered_channel = input("Enter a Telegram channel to scrape (username or invite link):\n").strip()
            if entered_channel == "":
                print("You must enter a valid channel name or invite link!\n")
                continue

            print(f"\nThis is the channel you provided:\n{entered_channel}\n")
            user_accepts = input(
                "Do you wish to proceed? Enter 'y' to continue or 'n' to start over:\n")

            if user_accepts.strip().lower() == 'y':
                self.target_channel = entered_channel
                channel_provided = True

        # Fetch channel entity to get the name
        try:
            self.channel_entity = await self.client.get_entity(self.target_channel)
            self.channel_name = self.channel_entity.title.replace(" ", "_") if self.channel_entity.title else "Unknown_Channel"
            print(f"Channel Name: {self.channel_name}")
        except errors.UsernameInvalidError:
            print("The channel username provided is invalid.")
            await self.client.disconnect()
            exit(1)
        except errors.ChannelPrivateError:
            print("The channel is private and you are not a member.")
            await self.client.disconnect()
            exit(1)
        except Exception as e:
            print(f"An unexpected error occurred while fetching the channel: {e}")
            await self.client.disconnect()
            exit(1)

        self.folder_name = f"Output_{self.channel_name}_{self.today_date}"

        try:
            os.mkdir(self.folder_name)
        except FileExistsError:
            pass
        print(f"\nCreated folder '{self.folder_name}' to store output\n")

        pulled_messages = await self.pull_messages_in_batches()
        cleaned_messages = self.parse_raw_messages(pulled_messages)
        self.create_messages_table(cleaned_messages)
        print(f"[Finished]")

    async def pull_messages_in_batches(self):
        # Define the message limit
        MESSAGE_LIMIT = 100
        print(f"Preparing to pull up to {MESSAGE_LIMIT} messages from '{self.channel_name}'\n")

        pulled_messages = []
        try:
            async for message in self.client.iter_messages(
                self.channel_entity, 
                limit=MESSAGE_LIMIT,
                reverse=True):  # Fetch from oldest to newest
                pulled_messages.append(message)
        except Exception as e:
            print(f"An error occurred while pulling messages: {e}")
            await self.client.disconnect()
            exit(1)

        print(f"Pulled {len(pulled_messages)} total messages for channel '{self.channel_name}'\n")
        return pulled_messages

    def parse_raw_messages(self, pulled_messages):
        print("Extracting fields and cleaning messages\n")
        cleaned_messages = []
        for message in pulled_messages:
            cleaned_messages.append(self.extract_message_fields(message))
        return cleaned_messages

    def extract_message_fields(self, message):
        # Message info: https://docs.telethon.dev/en/stable/quick-references/objects-reference.html
        cleaned = {}

        cleaned['message_id'] = getattr(message, 'id', None)
        cleaned['channel_name'] = getattr(self.channel_entity, 'title', 'Unknown_Channel')
        cleaned['message_date'] = str(getattr(message, 'date', None))
        cleaned['post_author'] = getattr(message, 'post_author', None)
        cleaned['is_posted_by_bot'] = getattr(message, 'via_bot_id', None)
        cleaned['total_replies'] = getattr(getattr(message, 'replies', None), 'replies', None)
        cleaned['is_reply_comments'] = getattr(getattr(message, 'replies', None), 'comments', None)
        cleaned['recent_replier_ids'] = [
            i.user_id for i in getattr(getattr(message, 'replies', None), 'recent_repliers', [])] if getattr(getattr(message, 'replies', None), 'recent_repliers', None) else []
        cleaned['raw_text'] = getattr(message, 'raw_text', None)

        return cleaned

    def create_messages_table(self, cleaned_messages):
        df = pd.DataFrame(cleaned_messages)
        if 'recent_replier_ids' in df.columns:
            df = df.explode("recent_replier_ids")  # Each replier ID in separate row
        df.fillna("", inplace=True)
        df.drop_duplicates(inplace=True)
        # Save to CSV with channel name
        csv_filename = f"{self.folder_name}.csv"
        df.to_csv(os.path.join(self.folder_name, csv_filename), index=False)
        print(f"Created file '{csv_filename}' in output folder '{self.folder_name}'\n\n")

    async def run(self):
        await self.start_client()
        await self.get_messages()
        await self.client.disconnect()

if __name__ == "__main__":
    scraper = TelegramChannelScraper()
    asyncio.run(scraper.run())
