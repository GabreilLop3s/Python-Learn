# função de potência de um número
power = lambda num: num ** 2
print(power(5))
print(power(78))

# pra saber se é par
se_par = lambda x: x % 2 == 0
print(se_par(10), se_par(7))

# função que divide um número por outro
divid = lambda x, y: x / y
print(divid(10, 2))

# reverse string
reverse = lambda s: s[::-1]
print(reverse("Python"))

# funcionalidades relacionadas aos filmes
movies_list = ["Titanic", "The GodFather", "Inception", "Jurassic Park", "The Matrix"]
rating = {
    "Titanic": [8.5, 9.0, 7.0],
    "The GodFather": [7.0, 8.5, 9.0],
    "Inception": [9.0, 10.0, 8.0],
    "Jurassic Park": [8.0, 7.0, 7.5],
    "The Matrix": [10.0, 8.0, 9.0]
}

# função que verifica se um filme está na lista
check_movie = lambda movie_name: movie_name in movies_list
print(check_movie("Titanic"), check_movie("Avatar"))

# função para calcular avaliação média
average_rating = lambda movie_name: sum(rating[movie_name]) / len(rating[movie_name])

# função para recomendar um filme com base na avaliação média
recommend_movie = lambda movie_name: f"Recomendo assistir '{movie_name}' com média de {average_rating(movie_name):.2f}"

print(f"Média de avaliação do filme The Matrix: {average_rating('The Matrix'):.2f}")
print(recommend_movie("Inception"))
