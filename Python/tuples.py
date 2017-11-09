# function input
my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}



tuple_data = [(d, a) for d, a in my_dict.iteritems()]

print tuple_data



#function output
#[("Speros", "(555) 555-5555"), ("Michael", "(999) 999-9999"), ("Jay", "(777) 777-7777")]
