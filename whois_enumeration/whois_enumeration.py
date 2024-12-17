import whois

# Sacar la informacion de whois 
domain_name = "udemy.com"
response = whois.whois(domain_name)
print(response)



