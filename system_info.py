import psutil
import platform


def get_battery():

    battery = psutil.sensors_battery()

    if battery:

        return (
            f"Your battery is at "
            f"{battery.percent} percent."
        )

    return "I couldn't find your battery information."


def get_system_info():

    system = platform.system()
    release = platform.release()
    processor = platform.processor()


    return (
        f"You are running {system} {release}. "
        f"Your processor is {processor}."
    )


def get_ram():

    memory = psutil.virtual_memory()

    ram_gb = round(
        memory.total / (1024 ** 3),
        2
    )

    used_gb = round(
        memory.used / (1024 ** 3),
        2
    )


    return (
        f"You have {ram_gb} gigabytes of RAM. "
        f"{used_gb} gigabytes are currently being used."
    )