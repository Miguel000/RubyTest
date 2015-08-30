puts 'Digame el año inicial'
year1 = gets.chomp.to_i
puts 'Ahora el final'
year2 = gets.chomp.to_i

fin = year2 - year1
ini = 0
puts
while ini.to_i < fin.to_i

	if (year1 % 4 ) == 0 and (year1 % 100 != 0)
		puts 'año bisiesto ' + year1.to_s
	end
	year1 = year1 +1
	ini = ini +1
end
