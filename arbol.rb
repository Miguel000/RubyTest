class ArbolNaranja

	def initialize
		@altura= 21
		@naranjas=0
		@anos=0
		puts 'El arbol tiene ' + @altura.to_s + 'años'
	end

	def altura
		puts @altura.to_s
	end
	
	def paso365Dias
		@anos = @anos + 1
		@altura = @altura + @anos*4
		if @anos > 100
			daFrutas = true
			@naranjas =  @naranjas + @anos*2
		end
		if @anos > 1000
				puts 'El arbol se muere de mayor'
				exit
		end
	end
	
	def contarNaranjas
		puts  @naranjas.to_s
	end

	def tomarNaranjas
		if @naranjas > 0
			@naranjas = @naranjas -1
			puts 'la naranja era deliciosa'
		else
			puts 'Este año no hay mas naranjas'
		end
	end

end

Arbol = ArbolNaranja.new
while 1
Arbol.paso365Dias
Arbol.paso365Dias
Arbol.paso365Dias
Arbol.paso365Dias
Arbol.altura
Arbol.contarNaranjas
Arbol.tomarNaranjas
end
