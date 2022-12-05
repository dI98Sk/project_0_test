"""Новая верси игры, сам загадывает и сам угадывает """
import numpy as np

def random_predict(number:int=1) -> int:
    """ Рандомно угадываем число

    Args:
        number (int, optional): Загадоное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    
    while True:
        count += 1
        predict_nummber = np.random.randint(1,101) #Предпологаемое число 
        if number == predict_nummber:
            break
    return (count)

def score_game(random_predict) -> int:
    """Сколько в среднем угадывает за 1000 подходов

    Args:
        random_predict (_type_): Функция угадывани

    Returns:
        int: Среднее количество угадываний 
    """
    
    count_ls = []
    np.random.seed(1) # Фиксируем сид дляя воспроизведения
    randon_array = np.random.randint(1,101, size=(1000)) # задали список наших чисел
    
    for number in randon_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток ')
    return(score)


#if __name__ == '__main__':
score_game(random_predict)