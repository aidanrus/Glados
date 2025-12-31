from loguru import logger
import sounddevice as sd
import soundfile as sf
from typing import Optional
from glados.utils.resources import resource_path

def play_audio_sound_effect(path: Optional[str] = None, sample_rate: Optional[int] = None, interruptible: Optional[bool] = True, block: Optional[bool] = None) -> None:

    # check if inputted audio file path exists, and default to error sound if not
    if resource_path(path).exists():
        preset_path = resource_path(path)
    else:
        logger.error("Audio preset not found: %s", preset_path)
        preset_path = resource_path("src/glados/assets/sounds/announcement.wav")

    # then play the sound effect
    try:
        import soundfile as sf

        preset_audio, preset_sr = sf.read(preset_path, dtype="float32")
        if preset_sr != sample_rate:
            logger.warning(
            "Preset sample rate (%s) differs from TTS sample rate (%s). "
            "Consider creating the WAV with the same sample rate.",
            preset_sr,
            sample_rate,
            )
        sd.play(preset_audio, preset_sr)

        # optionally remove this code to allow overlapping playback 
        # nvm doesnt work lol
        if not interruptible:
            sd.wait()

    except Exception as e:
        logger.error(f"Failed to play preset sound effect: {e}")

__all__ = ["play_audio_sound_effect"]