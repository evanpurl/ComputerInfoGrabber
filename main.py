import json

import psutil

from aiohttp import web

routes = web.RouteTableDef()


async def get_cpu_ram_usage():
    result_dict = dict()
    result_dict["CPU Usage:"] = f"{psutil.cpu_percent()} %"
    result_dict["CPU Temp:"] = f"{psutil.sensors_temperatures(fahrenheit=False)['k10temp'][0].current:.2f} C"
    result_dict["Ram Usage:"] = f"{psutil.virtual_memory()[2]} %"

    return result_dict


@routes.get('/')
async def get_info(request):
    return web.Response(text=json.dumps(await get_cpu_ram_usage()))


app = web.Application()
app.add_routes(routes)
web.run_app(app, port=7780)
