#!/bin/bash
python processPhrase.py palavra2Unigramas.txt palavra2Bigramas.txt fosseParametrizacao.txt palavra2Frases.txt > palavra2Resultado.txt
python processPhrase.py palavra1Unigramas.txt palavra1Bigramas.txt criamParametrizacao.txt palavra1Frases.txt > palavra1Resultado.txt