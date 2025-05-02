import argparse
from .ue5_resource_handler import UE5ResourceHandler

def main():
    parser = argparse.ArgumentParser(description="UE5 Resource Handler CLI")
    subparsers = parser.add_subparsers(dest="command")

    pak_parser = subparsers.add_parser("extract-pak", help="Извлечь .pak файл")
    pak_parser.add_argument("--pak", required=True)
    pak_parser.add_argument("--out", required=True)
    pak_parser.add_argument("--unrealpak", required=True)

    args = parser.parse_args()

    if args.command == "extract-pak":
        handler = UE5ResourceHandler(args.unrealpak)
        handler.extract_pak(args.pak, args.out)
        print("Извлечение завершено.")

if __name__ == "__main__":
    main()