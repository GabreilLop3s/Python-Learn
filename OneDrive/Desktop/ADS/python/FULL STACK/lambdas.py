"""função de potencia de um numero"""

power = lambda num: num ** 2
print(power(5))
print(power(78))


#pra saber se é par 
se_par =  lambda x: x % 2 == 0

#funcao que divide um numero por outro 
divid = lambda x, y : x / y 

#reverse string 
reverse = lambda s: s[::-1]

#funcionalidades relacionadas aos filmes:
movies_list = ["Titanic", "The GodFather", "Inception", "Jurassic Park", "The Matrix"]
rating = {
    "Titanic" : [8.5, 9.0, 7.0],
    "The GodFather" : [7.0, 8.5, 9.0],
    "Inception" : [9.0, 10.0, 8.0],
    "Jurassic Park" : [8.0, 7.0, 7.5],
    "The Matrix" : [10.0, 8.0, 9.0]
}

#função que verifica se um fikme esta na lista:
check_movie = lambda movie_name: movie_name in movies_list

#função para recomendar um filme com base na avaliação média:
recommend_movie = lambda movie_name: f"recomendo assistir {movie_name} com media na {avarage_rating(movie_name):2f}"



avarage_rating = lambda movie_name: sum(rating[movie_name]) / len(rating[movie_name])

print(f"Média de avaliação do filme The Matrix: {avarage_rating("The Matrix")}")






