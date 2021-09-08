#!/usr/bin/python

import whois

target = "google.com"


def func_whois(_domain):
    querywhois = whois.query(_domain)
    print("[+] - Nome dominio", querywhois.name)
    print("[+] - Data criação", querywhois.creation_date)
    print("[+] - Data de expiração", querywhois.expiration_date)
    print("[+] - Data da ultima atualização", querywhois.last_updated)
    print("[+] - Servidor whois registrado", querywhois.registrar)

    for _domain in querywhois.name_servers:
        print("[+] - Servidor de nomes: ", _domain)

func_whois(target)
