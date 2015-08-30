comando = ''
veces = 0

while (veces < 3)
	comando = gets.chomp
	if(comando == 'ADIOS')
		veces = veces + 1
	else 
		puts 'HUH?! ¡HABLA MAS FUERTE, HIJO!'
		veces = 0
	end
end
num = (rand(1929..1951))
puts 'NO, ¡NO DESDE '+ num.to_s + '!'
