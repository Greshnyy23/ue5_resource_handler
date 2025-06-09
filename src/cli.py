import argparse
from .ue5_resource_handler import UE5ResourceHandler

def main():
    parser = argparse.ArgumentParser(description="UE5 Resource Handler CLI")
    subparsers = parser.add_subparsers(dest="command")

    pak_parser = subparsers.add_parser("extract-pak", help="Извлечь .pak файл")
    pak_parser.add_argument("--pak", required=True)
    pak_parser.add_argument("--out", required=True)
    pak_parser.add_argument("--unrealpak", required=True)

    ucas_parser = subparsers.add_parser("parse-ucas", help="Разобрать .ucas/.utoc")
    ucas_parser.add_argument("--ucas", required=True)
    ucas_parser.add_argument("--utoc", required=True)

    ubulk_parser = subparsers.add_parser("extract-ubulk", help="Экспорт .ubulk")
    ubulk_parser.add_argument("--ubulk", required=True)
    ubulk_parser.add_argument("--out", required=True)

    args = parser.parse_args()

    if args.command == "extract-pak":
        handler = UE5ResourceHandler(args.unrealpak)
        handler.extract_pak(args.pak, args.out)
        print("Извлечение завершено.")
    elif args.command == "parse-ucas":
        handler = UE5ResourceHandler()
        handler.parse_ucas(args.ucas, args.utoc)
        print("Парсинг завершен.")
    elif args.command == "extract-ubulk":
        handler = UE5ResourceHandler()
        handler.extract_ubulk(args.ubulk, args.out)
        print("Экспорт завершен.")

if __name__ == "__main__":
    main()
