import requests
from requests.structures import CaseInsensitiveDict
import time
from datetime import datetime
from discord_webhook import DiscordWebhook, DiscordEmbed

headers = CaseInsensitiveDict()
headers["authorization"] = "enter your Auth key here"

def credits_today():
  time.sleep(0.5)
  r = requests.get("https://dashboard.honeygain.com/api/v1/earnings/today", headers=headers)
  e = r.json()["total"]["credits"]
  return e

def winning_credits():
  time.sleep(0.5)
  r = requests.get("https://dashboard.honeygain.com/api/v1/earnings/today", headers=headers)
  e = r.json()["winning_credits"]
  return e

def referral_credits():
  time.sleep(0.5)
  r = requests.get("https://dashboard.honeygain.com/api/v1/earnings/today", headers=headers)
  e = r.json()["referral_credits"]
  return e

def streaming_seconds():
  time.sleep(0.5)
  r = requests.get("https://dashboard.honeygain.com/api/v1/earnings/today", headers=headers)
  e = r.json()["streaming_seconds"]
  return e

def credits():
  time.sleep(0.5)
  r = requests.get("https://dashboard.honeygain.com/api/v1/users/balances", headers=headers)
  e = r.json()["data"]["payout"]["credits"]
  return e

def active_devices():
  time.sleep(0.5)
  r = requests.get("https://dashboard.honeygain.com/api/v1/users/me", headers=headers)
  e = r.json()["data"]["active_devices_count"]
  return e

def total_devices():
  time.sleep(0.5)
  r = requests.get("https://dashboard.honeygain.com/api/v1/users/me", headers=headers)
  e = r.json()["data"]["total_devices"]
  return e
  
while True:
  now = datetime.now()
  ctime = now.strftime("%H:%M")
  if str(ctime) == "19:00":
    webhook = DiscordWebhook(url='enter your webhook URL here')
    total_percent = round(float(credits()) / 200, 1)
    embed = DiscordEmbed(title='Honeygain Stats', color='03b2f8')
    embed.add_embed_field(name='Earned today', value=credits_today())
    embed.add_embed_field(name='Total credits', value=f'{credits()}/20000 ({total_percent}%)')
    embed.add_embed_field(name='Credits won today', value=winning_credits())
    embed.add_embed_field(name='Referral credits', value=referral_credits())
    embed.add_embed_field(name='Streaming seconds', value=streaming_seconds())
    embed.add_embed_field(name='Active Devices:', value=f'{active_devices()}/{total_devices()}')
    webhook.add_embed(embed)
    response = webhook.execute()
    time.sleep(60)
  else:
    time.sleep(50)
