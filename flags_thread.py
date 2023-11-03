from concurrent import futures
from flag import save_flag, get_flag, main

def download_one(cc):
    image = get_flag(cc)
    save_flag(image,f'{cc}.gif')
    print(cc,end='\n')
    return cc

def download_many(cc_list):
    with futures.ThreadPoolExecutor() as exec:
        res = exec.map(download_one,sorted(cc_list))
    return len(list(res))

if __name__ == '__main__':
    main(download_many)