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
        assert_equals 1, @myproblem.factor(1);
        assert true
    end
end
