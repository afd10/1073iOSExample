require 'Problem3'
require 'test/unit'

class Problem3Test < Test::Unit::TestCase

    def setup
        @myproblem = Problem3.new
    end

    def test_truth
        assert true
    end

    def test_factoring
		assert_equal [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], @myproblem.sieveOfE(30)
	end

	def test_largestFactor
		assert_equal 29, @myproblem.largestFactor(13195)
	end

end
