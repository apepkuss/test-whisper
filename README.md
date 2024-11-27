# Tools for testing whisper

## convert_to_srt.py

Converts a text file with timestamped lines to SRT subtitle format.

Usage:

```bash
python convert_to_srt.py input.txt output.srt
```

The input.txt file looks like this:

```text
[00:00:00.000 --> 00:00:02.480]  Yeah, so thank you for being here.\n[00:00:02.480 --> 00:00:05.600]  So my name is Sebastien Crozet, and I\n[00:00:05.600 --> 00:00:08.880]  will be talking about the Rapier physics engine.\n[00:00:08.880 --> 00:00:13.760]  But first, let's start with a few questions.\n[00:00:13.760 --> 00:00:18.480]  How would you try to train a robot\n[00:00:18.480 --> 00:00:22.040]  to evolve in a terrain like Mars?\n[00:00:22.040 --> 00:00:28.680]  Or how would you train a robot to operate in, I don't know.
```

The output.srt file looks like this:

```srt
1
00:00:00,000 --> 00:00:02,480
Yeah, so thank you for being here.

2
00:00:02,480 --> 00:00:05,600
So my name is Sebastien Crozet, and I

3
00:00:05,600 --> 00:00:08,880
will be talking about the Rapier physics engine.

4
00:00:08,880 --> 00:00:13,760
But first, let's start with a few questions.

5
00:00:13,760 --> 00:00:18,480
How would you try to train a robot

6
00:00:18,480 --> 00:00:22,040
to evolve in a terrain like Mars?

7
00:00:22,040 --> 00:00:28,680
Or how would you train a robot to operate in, I don't know
```
