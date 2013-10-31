from __future__ import absolute_import
from powerline.theme import requires_segment_info
import redis

@requires_segment_info
def mic_status(pl, segment_info, filename="/tmp/natlink_status.txt"):
  r = redis.Redis()
  try:
    status = r.get('natlink.mic') 
    if status == 'on':
      return [{
        "contents": "mic on",
        "highlight_group": "mic_on"
        }]
    if status == 'off':
      return [{
        "contents": "mic off",
        "highlight_group": "mic_off"
        }]
    if status == 'sleeping':
      return [{
        "contents": "mic asleep",
        "highlight_group": "mic_sleeping"
        }]
    return None
  except OSError as e:
    raise

