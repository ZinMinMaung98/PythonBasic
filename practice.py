def funfcopy(soc,dist):
    with open(soc,'r') as fi:
        with open(dist,'w') as fo:
            for line in fi:
                fo.write(line)

def main():
    funfcopy('proj','copyfile')

if __name__ == '__main__':
    main()



