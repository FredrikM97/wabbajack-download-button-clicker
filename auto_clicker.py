import os
import sys
import time
import signal
import argparse
from dataclasses import dataclass

import pyautogui
import keyboard


# -------------------- CONFIG --------------------

@dataclass
class Config:
    image_path: str
    confidence: float
    retry_attempts: int
    retry_delay: float
    loop_delay: float
    exit_hotkey: str


# -------------------- ARGUMENT PARSING --------------------

def parse_arguments() -> Config:
    parser = argparse.ArgumentParser(description="Auto click image on screen")

    parser.add_argument("--image", required=True, help="Absolute path to image file")
    parser.add_argument("--confidence", type=float, default=0.8)
    parser.add_argument("--retries", type=int, default=3)
    parser.add_argument("--retry-delay", type=float, default=0.5)
    parser.add_argument("--loop-delay", type=float, default=7.0)
    parser.add_argument("--exit-hotkey", default="ctrl+shift+e")
    parser.add_argument(
        "--speed",
        choices=["slow", "normal", "fast"],
        default="normal",
        help="Preset timing profile"
    )

    args = parser.parse_args()

    retry_delay, loop_delay = apply_speed_preset(
        args.speed,
        args.retry_delay,
        args.loop_delay
    )

    return Config(
        image_path=args.image,
        confidence=args.confidence,
        retry_attempts=args.retries,
        retry_delay=retry_delay,
        loop_delay=loop_delay,
        exit_hotkey=args.exit_hotkey
    )


def apply_speed_preset(speed: str, retry_delay: float, loop_delay: float):
    if speed == "slow":
        return 1.0, 10.0
    if speed == "fast":
        return 0.2, 3.0
    return retry_delay, loop_delay


# -------------------- UTILITIES --------------------

def validate_image_path(path: str) -> None:
    if not os.path.isfile(path):
        print(f"[ERROR] Image file not found:\n{path}")
        sys.exit(1)


def click_on_image(config: Config) -> bool:
    for attempt in range(1, config.retry_attempts + 1):
        try:
            location = pyautogui.locateOnScreen(
                config.image_path,
                confidence=config.confidence
            )

            if location:
                center = pyautogui.center(location)
                original_position = pyautogui.position()

                print(f"[✓] Found at {center} (attempt {attempt})")
                pyautogui.click(center)
                pyautogui.moveTo(original_position)

                return True

            print(f"[{attempt}/{config.retry_attempts}] Not found")
            time.sleep(config.retry_delay)

        except Exception as e:
            print(f"[ERROR] {e}")
            time.sleep(config.retry_delay)

    print("[!] Not found after retries")
    return False


# -------------------- MAIN LOOP --------------------

running = True


def stop_program():
    global running
    running = False
    print("\n[INFO] Shutting down...")


def run_loop(config: Config):
    while running:
        click_on_image(config)
        time.sleep(config.loop_delay)


def main():
    config = parse_arguments()
    validate_image_path(config.image_path)

    print("Move this console window so it doesn't block the button.")
    input("Press Enter to start...\n")

    keyboard.add_hotkey(config.exit_hotkey, stop_program)
    print(f"[INFO] Press {config.exit_hotkey.upper()} to stop.\n")

    run_loop(config)


# -------------------- ENTRY POINT --------------------

if __name__ == "__main__":
    signal.signal(signal.SIGINT, lambda s, f: stop_program())
    main()