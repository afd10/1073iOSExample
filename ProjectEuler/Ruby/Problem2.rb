#!/usr/bin/env ruby

class Problem2
	def fib(limit)
		fibs = [1,2] 
		current = 2
		last = 1
		nextfib = current + last
		while (nextfib < limit)
			fibs.push(nextfib)
			last = current
			current = nextfib
			nextfib = last + current
		end

		return fibs
	end

	def isEven(number)
		return number%2 == 0
	end

	def evenSums(number)
		sum = 0
		fibs = self.fib(number)
		fibs.each do |x|
			if self.isEven(x)
				sum = sum + x
			end
		end
		return sum

	end

end

n = Problem2.new
puts n.evenSums(4000000)

