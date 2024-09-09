# feed-client

Read this in other languages: [English](README.md), [日本語](README.ja.md).

<!-- TOC -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#description">Description</a></li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

## Description

`feed-client` is a Python client program for the SYNESIS Feed Service. It allows users to stream captured packets from SYNESIS over a socket connection.

![image](https://github.com/user-attachments/assets/b9c46775-2f5e-4517-9f5f-2615dc2f22ac)


1. SYNESIS/Capture: Receives packets via the network card (NIC).
2. SYNESIS/ Capture: Stores packets in the packet data area.
3. Client/Client program: Requests packets from SYNESIS/Feed Service in TCP/IP.
4. SYNESIS/Feed Service: Reads packets from the packet data area.
5. SYNESIS/Feed Service: Send packets to the request source in TCP/IP.

## Installation
`feed-client` is implemented as a single-file Python script. You can download the main script file, `src/feed_client/main.py`, and execute it directly.
``` shell
$ python main.py
```

Alternatively, `feed-client` can be installed with pip or pipx.
``` shell
$ pip install git+https://github.com/synesis-toyo/feed-client.git
```

## Usage

### Synopsis
```
feed-client [-h] [-f {pcap,pcapng,scap}] [-c [{A,B,C,D,E,F,G,H,all} [{A,B,C,D,E,F,G,H,all} ...]]] [-a X.X.X.X] [-p PORT] [-s START] [-e END] [-z SIZE] [-o OUTPUT]
```

### Options

| Option             | Description                                                               | Value Range                                                                                                                               | Default Value   |
|--------------------|---------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|-----------------|
| `-h`, `--help`     | Displays the help message.                                                | -                                                                                                                                         | -               |
| `-f`, `--format`   | Specifies the output file format.                                         | `pcap`: pcap format (nanoseconds)<br>`pcapng`: pcapng format<br>`scap`: scap format                                                       | `pcap`          |
| `-c`, `--channels` | Specifies the channel(s) to read from.                                    | `A～H` or `all`<br>Separate channels with a space to specify multiple channels.                                                           | `A`             |
| `-a`, `--address`  | Specifies the IP address of SYNESIS                                       | IPv4 address                                                                                                                              | `127.0.0.1`     |
| `-p`, `--port`     | Specifies the TCP port of the Feed Service                                | Integer between 1 and 65535.                                                                                                              | `9060`          |
| `-s`, `--start`    | Specifies the start time for reading captured packets.                    | `0` or `YYYY-mm-dd_HH-MM-SS`<br>When `0`, packat capture data is streamed from the beginning of the latest capture session. | `0`             |
| `-e`, `--end`      | Specifies the end time for reading captured packets.                      | `0` or `YYYY-mm-dd_HH-MM-SS`<br>When `0`, packat capture data is streamed until the end of the latest capture session.            | `0`             |
| `-z`, `--size`     | Specifies the maximum size of message the client can receive in kilobytes | Integer greater than or equal to `1`                                                                                                      | `1`             |
| `-o`, `--output`   | Specifies the output filename to store the streamed packet data.          | Filename                                                                                                                                  | Standard output |

## License  
© TOYO Corporation  
Licensed under the [MIT License](https://github.com/synesis-toyo/FeedService?tab=MIT-1-ov-file).

## Contact
https://www.synesis.tech/  
[synesis-globalsales@toyo.co.jp](<mailto:synesis-globalsales@toyo.co.jp>)



