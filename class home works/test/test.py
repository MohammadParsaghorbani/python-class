import qrcode

# name = input("name: ")
qrcode.make('https://github.com/MohammadParsaghorbani/django_test/tree/main/posts/templates/posts').save("qr.png")
