from jnius import autoclass
from time import sleep



def android_record(output):
    
    # get the needed Java classes
    MediaRecorder = autoclass('android.media.MediaRecorder')
    AudioSource = autoclass('android.media.MediaRecorder$AudioSource')
    OutputFormat = autoclass('android.media.MediaRecorder$OutputFormat')
    AudioEncoder = autoclass('android.media.MediaRecorder$AudioEncoder')

    # create out recorder
    mRecorder = MediaRecorder()
    mRecorder.setAudioSource(AudioSource.MIC)
    mRecorder.setOutputFormat(OutputFormat.MPEG_4)
    mRecorder.setOutputFile(output)
    mRecorder.setAudioEncoder(AudioEncoder.AAC)
    mRecorder.prepare()

    # record 5 seconds
    mRecorder.start()
    sleep(3)
    mRecorder.stop()
    mRecorder.release()
    return True

def play_audio(source):
    # get the MediaPlayer java class
    MediaPlayer = autoclass('android.media.MediaPlayer')

    # create our player
    mPlayer = MediaPlayer()
    mPlayer.setDataSource(source)
    mPlayer.prepare()

    # play
    print('duration:', mPlayer.getDuration())
    mPlayer.start()
    print('current position:', mPlayer.getCurrentPosition())
    sleep(3)

    # then after the play:
    mPlayer.release()
    return True
