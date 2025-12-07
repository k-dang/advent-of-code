# invalid Ids are any ID which is made only of some sequence of digits repeated twice
# 55 - 5 twice
# 6464 - 64 twice
# 123123 - 123 twice

# find all of the invalid IDs that appear in the given ranges
# 11 - 22 - 2 invalid IDs 11 and 22
# 95 - 115 has one, 99
# 998 - 1012 has one, 1010

# no leading zeros (0101) is not an ID
# 101 is a valid ID


def part_one(ids):
    id_ranges = ids.split(",")
    sum_of_invalid_ids = 0

    for id_range in id_ranges:
        # check every number in between start and end
        # we only care about the even numbers?
        start, end = id_range.split("-")
        for i in range(int(start), int(end) + 1):
            num_digits = len(str(i))
            if num_digits % 2 == 0:
                # only care about the even numbers

                # get each half and check if they are the same
                half1 = str(i)[: num_digits // 2]
                half2 = str(i)[num_digits // 2 :]
                if half1 == half2:
                    print("invalid ID:", i)
                    sum_of_invalid_ids += i

    return sum_of_invalid_ids


# part two
# an ID is invalid if it is made only of some sequence of digits repeated AT LEAST twice
# 12341234 - 1234 twice
# 123123123 - 123 3 times
# 1212121212 - 12 5 times
# 1111111 - 1 7 times
# are all invalid IDs

# sequence should still make up all the digits
# if 2 digits, then 1 & 1
# 3 digits, then 1 & 1 & 1 - 1 digit is repeated 3 times
# 4 digits, 2 & 2 and 1 digit is repeated 4 times
# 5 digits, 1 digit is repeated 5 times
# 6 digits - 1, 2, 3
# 7 digits - 1
# 8 digits - 1, 2, 4
# 9 digits - 1, 3
# we want all the values that perfectly divide into that number


def get_factors(num):
    factors = []
    for i in range(1, num):  # don't include the number itself
        if num % i == 0:
            factors.append(i)
    return factors


def part_two(ids):
    id_ranges = ids.split(",")
    sum_of_invalid_ids = 0

    # acount for duplicates

    for id_range in id_ranges:
        start, end = id_range.split("-")
        for i in range(int(start), int(end) + 1):
            num_digits = len(str(i))
            factors = get_factors(num_digits)
            for factor in factors:
                values = [str(i)[x : x + factor] for x in range(0, len(str(i)), factor)]
                # print("values:", values)
                result = all(value == values[0] for value in values)
                if result:
                    # print("invalid ID:", i)
                    sum_of_invalid_ids += i
                    break

    return sum_of_invalid_ids


if __name__ == "__main__":
    ids = "12077-25471,4343258-4520548,53-81,43661-93348,6077-11830,2121124544-2121279534,631383-666113,5204516-5270916,411268-591930,783-1147,7575717634-7575795422,8613757494-8613800013,4-19,573518173-573624458,134794-312366,18345305-18402485,109442-132958,59361146-59451093,1171-2793,736409-927243,27424-41933,93-216,22119318-22282041,2854-4778,318142-398442,9477235089-9477417488,679497-734823,28-49,968753-1053291,267179606-267355722,326-780,1533294120-1533349219"
    # test_ids = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
    # test_ids = "222220-222224"
    result = part_one(ids)
    print("result:", result)

    result = part_two(ids)
    print("result:", result)
