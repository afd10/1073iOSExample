require 'Problem1'
require 'test/unit'

class Problem1Test < Test::Unit::TestCase

    def setup
        @myproblem = Problem1.new
    end

    def test_truth
        assert true
    end

    def test_factoring
        assert_equal [1], @myproblem.factor(1)
		assert_equal [1,2], @myproblem.factor(2)
		assert_equal [1,2,5,10], @myproblem.factor(10)
	end

	def test_factored_by_3
		assert_equal false, @myproblem.isAFactor?(3,1)
		assert_equal true, @myproblem.isAFactor?(3,3)
	end

	def test_sum_of_multiples
		assert_equal 23, @myproblem.sumOfMultiples(10);
	end
end
