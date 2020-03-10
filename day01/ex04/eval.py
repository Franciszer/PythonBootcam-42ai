class	Evaluator:
	def	check_len(self, coefs, words):
		return False if len(coefs) != len(words) else True
	def	zip_evaluate(self, coefs, words):
		if not self.check_len(coefs, words):
			return -1
		zip_sum = 0
		for vals in zip(coefs, words):
			zip_sum += vals[0] * len(vals[1])
		return (zip_sum)
	def	enumerate_evaluate(self, coefs, words):
		if not self.check_len(coefs, words):
			return -1
		enumerate_sum = 0
		for i, word in enumerate(words):
			enumerate_sum += len(word) * coefs[i]
		return (enumerate_sum)
#
#
#words = ["Le", "Lorem", "Ipsum", "est", "simple"]
#coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
#evaluator = Evaluator()
#print(evaluator.enumerate_evaluate(coefs, words))