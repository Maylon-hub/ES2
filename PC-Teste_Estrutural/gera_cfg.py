from pathlib import Path 
import argparse
import os
import sys

# Adiciona o Graphviz local ao PATH
graphviz_bin = r"d:\GitHub\ES2\Teste Estrutural\graphviz\Graphviz-15.1.0-win64\bin"
os.environ["PATH"] += os.pathsep + graphviz_bin

from py2cfg import CFGBuilder


parser = argparse.ArgumentParser(
   description="Gera o CFG de um programa Python"
)
parser.add_argument("programa", help="arquivo .py de entrada")
parser.add_argument("saida", help="diretorio de saida")
args = parser.parse_args()
programa = Path(args.programa)
saida = Path(args.saida)
saida.mkdir(parents=True, exist_ok=True)
cfg_name = programa.stem
cfg = CFGBuilder().build_from_file(cfg_name, str(programa))
cfg.build_visual(cfg_name, "pdf", directory=str(saida))
print(f"CFG gerado em: {saida / (cfg_name + '.pdf')}")
