# recon-kit

Mapeador de reconocimiento para bug bounty. Descubre subdominios de un objetivo
y filtra cuáles están vivos, en un solo comando.

## Uso

```bash
python3 recon.py objetivo.com
```

Genera `objetivo.com_vivos.txt` con los hosts que responden.

## Cómo funciona

1. **subfinder** — enumeración pasiva de subdominios (registros de certificados, DNS histórico).
2. **httpx** — comprueba cuáles responden por HTTP/HTTPS (100 hilos, timeout de 5s).

## Requisitos

- Python 3
- [subfinder](https://github.com/projectdiscovery/subfinder)
- [httpx](https://github.com/projectdiscovery/httpx)

## Ética

Úsalo **solo** contra objetivos tuyos o con autorización explícita (programa de
bug bounty con scope definido). El escaneo no autorizado es ilegal.

---
por [0xkelvin](https://0xkelvin.sh)
