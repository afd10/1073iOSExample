#!/usr/bin/env ruby
require 'set'
class Problem3 
	def sieveOfE(limit)
		myrange = Array.new(limit-2) {|i| i+2}
		myrange.each do |i|
			myrange.delete_if {|num| (num %i ==0)and (num!=i)}
		end
		return myrange

	end

	def largestFactor(n)
		limit = Math.sqrt(n)
		self.sieveOfE(limit).reverse.each { |x| if n % x ==0: return x; end}
	end


	def factorList(n)
		factors = Array.new
		(1..Math.sqrt(n)).each do |i|
			if n%i ==0
				factors.push(i)
			end
		end
		return factors
	end

	def isPrime(n)
		if self.factorList(n) == [1]
			return true
		else
			return false
		end
	end

def largestPrimeFactor(n):
	factors = self.factorList(n)
	pfactors = Array.new
	factors.each{ |i| if n.isPrime(i): pfactors.push(i); end}
	return pfactors[-1]


end

n = Problem3.new
#puts n.largestFactor(13195)
#puts n.largestFactor(600851475143)
#n.sieveOfE(16a)
#
#puts n.isPrime(35)
#factors = n.factorList(13195)

puts pfactors
puts pfactors[-1];

