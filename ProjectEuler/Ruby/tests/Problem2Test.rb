require 'Problem2'
require 'test/unit'

class Problem2Test < Test::Unit::TestCase

    def setup
        @myproblem = Problem2.new
    end

    def test_truth
        assert true
    end

    def test_fib_sequence
		assert_equal [1, 2, 3, 5, 8, 13, 21, 34, 55, 89], @myproblem.fib(100)
	end

	def test_even
		assert_equal TRUE, @myproblem.isEven(2)
		assert_equal FALSE, @myproblem.isEven(3)
	end

	def test_evenSums
		assert_equal 44, @myproblem.evenSums(100)
		end
end
