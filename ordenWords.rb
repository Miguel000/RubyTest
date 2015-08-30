# Recoger palabras hasta detectar vacio.
# Devolverlas ordenadas.

word = "z"
list = []

while word != ''
puts 'Dime nombre para añadirlo'
word = gets.chomp	
list.push word

end
print 'salida!'
nombre = gets
puts "Hola #{nombre}"
