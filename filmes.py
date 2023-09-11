from filmes.models import Filme

filme1 = Filme(titulo='veloses e furiosos 9', ano=2020, diretor='Diretor 1', genero='Ação')
filme1.save()

filme2 = Filme(titulo='Mulher Maravilha', ano=2018, diretor='Diretor 2', genero='Comédia')
filme2.save()