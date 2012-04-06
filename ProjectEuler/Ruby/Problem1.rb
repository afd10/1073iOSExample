#!/usr/bin/env ruby
require 'set'
class Problem1 
	
	def factor(number)
		factors = Set.new [];
    	(1..Math.sqrt(number)).each do |i|
			if number % i == 0
				factors.add(i);
				factors.add(number / i)
			end
		end
		return factors.to_a.sort
	end

	def isAFactor?(factor, number)
		return (number % factor == 0) 
	end

	def sumOfMultiples(target)
		sum = 0
		(1..(target-1)).each do |i|
			if (self.isAFactor?(3,i) or self.isAFactor?(5,i))
				sum =  sum + i
			end
		end
		return sum
	end
end
	
	
p =  Problem1.new
puts p.factor(1)
puts p.sumOfMultiples(1000)
