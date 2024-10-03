from Cliente import Cliente

cliente = Cliente("João", "12345678900")
print(cliente.ler_cpf())
cliente.mudar_cpf("12345")
print(cliente.ler_cpf())