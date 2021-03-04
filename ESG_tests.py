from unittest import TestCase

# reverse all words in the sentence
# ie.. I am a developer => developer a am I

def reverse_sentence(sentence):
    words = sentence.split()
    words.reverse()
    return ' '.join(words)

class TestReverseSentence(TestCase):
    def test_reverses_sentences_correctly(self):
        test_data = "I am a developer"
        expected = "developer a am I"
        self.assertEqual(expected, reverse_sentence(test_data))
        
# ###############################################
test_trades = [
  {"trader_id": 1, "value": -100.0, "date": "2016-06-01"},
  {"trader_id": 1, "value": 50, "date": "2016-06-01"},
  {"trader_id": 1, "value": 50, "date": "2016-06-02"},
  {"trader_id": 1, "value": 50, "date": "2016-06-02"},
  {"trader_id": 2, "value": 50, "date": "2016-06-02"}
]

test_traders = [
  {"id": 1, "name": "Rob"},
  {"id": 2, "name": "John"}
]

def calculate_trade_total(trades):
    trades_sum = 0
    for trade in trades:
        trades_sum += trade["value"]    
    return trades_sum

def calculate_trade_by_id(trades, id):
    trades_sum = 0
    for trade in trades:
        if trade["trader_id"] == id:
            trades_sum += trade["value"]
    return trades_sum

def calculate_trader_totals(trades, traders):
    result = {}
    for trade in traders:
        val = calculate_trade_by_id(trades, trade["id"])
        result[trade["name"]] = val
    return result

def calculate_trade_by_id_and_date(trades, id, date):
    trades_sum = 0
    for trade in trades:
        if trade["trader_id"] == id and trade["date"] == date:
            trades_sum += trade["value"]
    return trades_sum

def calculate_trader_totals_for_date(trades, traders, date):
    result = {}
    for trade in traders:
        val = calculate_trade_by_id_and_date(trades, trade["id"], date)
        result[trade["name"]] = val
    return result

class TestTradeAnalysis(TestCase):
    def test_calculate_trade_total_calculates_correct_value(self):
        result = calculate_trade_total(test_trades)
        expected = 100
        self.assertEqual(expected, result)

    def test_calculate_trader_totals_calculates_correct_values(self):
        result = calculate_trader_totals(test_trades, test_traders)
        expected = {"Rob": 50, "John": 50}
        self.assertEqual(expected, result)

    def test_calculate_trader_totals_for_date_works_for_1st_june(self):
        result = calculate_trader_totals_for_date(test_trades, test_traders, "2016-06-01")
        expected = {"Rob": -50, "John": 0}
        self.assertEqual(expected, result)

    def test_calculate_trader_totals_for_date_works_for_2nd_june(self):
        result = calculate_trader_totals_for_date(test_trades, test_traders, "2016-06-02")
        expected = {"Rob": 100, "John": 50}
        self.assertEqual(expected, result)

# ################################################

def rle_encode(string):
    if not string:
        return ""
    ch = string[0]
    n = 0
    result = ""
    for c in string:
        if ch != c:
            result += str(ch)
            result += str(n)            
            n = 1
            ch = c
        else:
            n += 1 
    result += str(ch)
    result += str(n)      
        
    return result

class TestRleEncode(TestCase):
    def test_encodes_the_input_correctly(self):

        test_data = "bbxxxxyeebbbbxool"

        expected = "b2x4y1e2b4x1o2l1"

        self.assertEqual(expected, rle_encode(test_data))
        
# ################################################


def find_matching_parenthesis2(text, parenthesis_index):
    n = 1
    for i in range(parenthesis_index + 1, len(text)):
        c = text[i]
        if c == '(':
            n += 1
        if c == ')':
            n -= 1
            if n == 0:
                return i
    return -1

def find_matching_parenthesis(text, parenthesis_index):
    n = 1
    if text[parenthesis_index] == '(':
        for i in range(parenthesis_index + 1, len(text)):
            c = text[i]
            if c == '(':
                n += 1
            if c == ')':
                n -= 1
                if n == 0:
                    return i

    if text[parenthesis_index] == ')':
        for i in reversed(range(0, parenthesis_index )):
            c = text[i]
            if c == ')':
                n += 1
            if c == '(':
                n -= 1
                if n == 0:
                    return i
                
    return -1

class TestFindMatchingParenthesis(TestCase):
    def test_return_index_of_matching_parenthesis(self):

        test_text = "Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing."
        test_index = 10

        expected = 79

        self.assertEqual(expected, find_matching_parenthesis(test_text, test_index))

    def test_bonus_question_for_clever_clogs(self):

        test_text = "Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing."
        test_index = 79

        expected = 10

        self.assertEqual(expected, find_matching_parenthesis(test_text, test_index))

print("Executing Tests")
TestReverseSentence().test_reverses_sentences_correctly()
print("Reverse Sentence Test Completed")
TestTradeAnalysis().test_calculate_trade_total_calculates_correct_value()
print("Trade Analysis Test 1 Complete")
TestTradeAnalysis().test_calculate_trader_totals_calculates_correct_values()
print("Trade Analysis Test 2 Complete")
TestTradeAnalysis().test_calculate_trader_totals_for_date_works_for_1st_june()
print("Trade Analysis Test 3 Complete")
TestTradeAnalysis().test_calculate_trader_totals_for_date_works_for_2nd_june()
print("Trade Analysis Test 4 Complete")
TestRleEncode().test_encodes_the_input_correctly()
print("Run Length Encoder Test Complete")
TestFindMatchingParenthesis().test_return_index_of_matching_parenthesis()
print("Parenthesis Test 1 Complete")
TestFindMatchingParenthesis().test_bonus_question_for_clever_clogs()
print("Parenthesis Test 2 Complete")
