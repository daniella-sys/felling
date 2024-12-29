import python_weather
import asyncio
import os

async def getweather() -> None:
    async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
        weather = await client.get('New York')
        print(weather.temperature)
        if __name__ == '__main__':
            asyncio.run(getweather())
