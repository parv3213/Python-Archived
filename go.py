def main():
    a=raw_input("::::-")
    try:
        int(a)
        return a
    except ValueError:
        print "Please enter from choices given"
        main()



print "OKK"
main()
print "Great"
