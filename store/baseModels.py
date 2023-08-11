from store import models


def initialize_categories():
    Category = models.Category
    Category.objects.get_or_create(
        category_name='Vetements', description="Catégorie de vêtements comprenant une variété de styles, de tailles et de designs.")

    Category.objects.get_or_create(
        category_name='Chaussures', description="Catégorie de chaussures comprenant des chaussures pour hommes, femmes et enfants dans différents styles et tailles.")

    Category.objects.get_or_create(
        category_name='Accessoires', description="Catégorie d'accessoires comprenant des articles tels que des sacs, des bijoux, des ceintures et plus encore.")

    Category.objects.get_or_create(
        category_name='Électronique', description="Catégorie d'électronique comprenant une large gamme de produits tels que des téléphones, des ordinateurs, des appareils audio et plus encore.")

    Category.objects.get_or_create(
        category_name='Alimentation', description="Catégorie d'alimentation comprenant des produits alimentaires de différentes catégories, des produits frais aux produits emballés.")

    Category.objects.get_or_create(category_name='Santé et beauté',
                                   description="Catégorie de santé et de beauté comprenant des produits de soins personnels, de maquillage, de soins de la peau et plus encore.")

    Category.objects.get_or_create(category_name='Maison et jardin',
                                   description="Catégorie de maison et de jardin comprenant des articles pour la maison tels que des meubles, des décorations, des ustensiles de cuisine et plus encore.")

    Category.objects.get_or_create(category_name='Sports et loisirs',
                                   description="Catégorie de sports et de loisirs comprenant des articles liés aux sports, aux activités de plein air, aux jeux et plus encore.")

    Category.objects.get_or_create(category_name='Livres et médias',
                                   description="Catégorie de livres et de médias comprenant une variété de livres, de films, de musique et de contenu multimédia.")

    Category.objects.get_or_create(
        category_name='Autres', description="Catégorie pour les articles qui ne rentrent pas dans les catégories précédentes, offrant une diversité d'options.")


if __name__ == "__main__":
    initialize_categories()
