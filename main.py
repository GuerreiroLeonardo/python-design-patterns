# from fila_normal import filanormal
# from fila_prioritaria import FilaPrioritaria
from FactoryMethod.line_factory import LineFactory

# fila_teste = filanormal()
# fila_teste.atualizafila()
# fila_teste.atualizafila()
# fila_teste.atualizafila()
# fila_teste.atualizafila()
# print(fila_teste.chamacliente(5))
# print(fila_teste.chamacliente(10))

# fila_teste_2 = FilaPrioritaria()
# fila_teste_2.atualizafila()
# fila_teste_2.atualizafila()
# fila_teste_2.atualizafila()
# print(fila_teste_2.chamacliente(10))
# print(fila_teste_2.estatistica("10/01/1993", 198, "detail"))

line_factory = LineFactory().get_line("normal")
line_factory.update_line()
line_factory.update_line()
line_factory.update_line()
print(line_factory.summon_client(10))
