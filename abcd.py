import asyncio
from shazamio import Shazam


async def main():
  shazam = Shazam()
  out = await shazam.recognize_song(r'C:\Users\14089\Downloads\Aaj Jane Ki Zid Na Karo - (Raag.Fm).mp3')
  print(out)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())