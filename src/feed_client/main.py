import argparse
import socket
import sys

format_map = {
    "pcap": "1",
    "pcapng": "2",
    "scap": "3",
}

channel_map = {
    "A": 0x01,
    "B": 0x02,
    "C": 0x04,
    "D": 0x08,
    "E": 0x10,
    "F": 0x20,
    "G": 0x40,
    "H": 0x80,
    "all": 0xFF,
}


def main():
    parser = argparse.ArgumentParser(
        description="Feed service client.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "-f",
        "--format",
        type=str,
        choices=format_map.keys(),
        default="pcap",
        help="format",
    )
    parser.add_argument(
        "-c",
        "--channels",
        type=str,
        nargs="*",
        choices=channel_map.keys(),
        default="A",
        help="channels",
    )
    parser.add_argument(
        "-a",
        "--address",
        type=str,
        default="127.0.0.1",
        metavar="X.X.X.X",
        help="server address",
    )
    parser.add_argument("-p", "--port", type=int, default=9060, help="server port")
    parser.add_argument(
        "-s", "--start", type=str, default="0", help="start time (YYYY-mm-dd_HH-MM-SS)"
    )
    parser.add_argument(
        "-e", "--end", type=str, default="0", help="end time (YYYY-mm-dd_HH-MM-SS)"
    )
    parser.add_argument("-z", "--size", type=int, default=1, help="buffer size in KB")
    parser.add_argument(
        "-o", "--output", type=str, default="stdio", help="file name to save"
    )
    args = parser.parse_args()

    channel_bits = 0
    for channel in args.channels:
        channel_bits |= channel_map[channel]

    commands = []
    commands.append(format_map[args.format])
    commands.append(str(channel_bits))
    commands.append(str(args.size))
    commands.append(args.start)
    commands.append(args.end)

    fb = sys.stdout.buffer
    if args.output != "stdio":
        fb = open(args.output, "wb")

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((args.address, args.port))
        sock.send((",".join(commands) + "\0").encode("utf-8"))
        while True:
            chunk = sock.recv(args.size * 1024)
            if chunk == b"":
                break
            fb.write(chunk)
    except KeyboardInterrupt:
        pass

    sock.close()
    if args.output != "stdio":
        fb.close()


if __name__ == "__main__":
    main()
