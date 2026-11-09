#!/usr/bin/env python3
import argparse
import subprocess

def buscar_subdominios(dominio):
    print(f"[*] Buscando subdominios de {dominio}...")
    resultado = subprocess.run(
        ["subfinder", "-d", dominio, "-silent"],
        capture_output=True, text=True
    )
    subs = resultado.stdout.strip().split("\n")
    return [s for s in subs if s]

def filtrar_vivos(subdominios):
    print(f"[*] Comprobando cuáles de {len(subdominios)} están vivos (esto puede tardar)...")
    entrada = "\n".join(subdominios)
    resultado = subprocess.run(
        ["httpx-toolkit", "-silent", "-threads", "100", "-timeout", "5"],
        input=entrada, capture_output=True, text=True
    )
    vivos = resultado.stdout.strip().split("\n")
    return [v for v in vivos if v]

def guardar(dominio, vivos):
    archivo = f"{dominio}_vivos.txt"
    with open(archivo, "w") as f:
        f.write("\n".join(vivos))
    print(f"[+] Guardado en: {archivo}")

def main():
    parser = argparse.ArgumentParser(description="recon-kit — mapea subdominios vivos de un objetivo autorizado")
    parser.add_argument("dominio", help="El dominio a analizar (ej: 0xkelvin.sh)")
    args = parser.parse_args()

    print(f"[*] recon-kit iniciando sobre: {args.dominio}")

    subs = buscar_subdominios(args.dominio)
    print(f"[+] Encontrados {len(subs)} subdominios")

    vivos = filtrar_vivos(subs)
    print(f"[+] {len(vivos)} están vivos:")
    for v in vivos:
        print(f"    {v}")

    guardar(args.dominio, vivos)

if __name__ == "__main__":
    main()
