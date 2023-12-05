class Range:
    source_start: int
    dest_start: int
    length: int

    def __init__(self, source_start: int, dest_start: int, length: int):
        self.source_start = source_start
        self.dest_start = dest_start
        self.length = length


def parse_map(path: str):
    with open(path, "r") as f:
        lines = f.read().splitlines()

    range_map: list[Range] = []
    for line in lines:
        dst_start, src_start, length = line.split(" ")
        range_map.append(Range(int(src_start), int(dst_start), int(length)))

    return range_map


def main():
    with open("input_seeds.txt", "r") as f:
        seeds = [int(seed) for seed in f.read().split(" ")]

    seed2soil = sorted(parse_map("input_seed2soil.txt"), key=lambda x: x.source_start, reverse=True)
    soil2fert = sorted(parse_map("input_soil2fert.txt"), key=lambda x: x.source_start, reverse=True)
    fert2water = sorted(parse_map("input_fert2water.txt"), key=lambda x: x.source_start, reverse=True)
    water2light = sorted(parse_map("input_water2light.txt"), key=lambda x: x.source_start, reverse=True)
    light2temp = sorted(parse_map("input_light2temp.txt"), key=lambda x: x.source_start, reverse=True)
    temp2humid = sorted(parse_map("input_temp2humid.txt"), key=lambda x: x.source_start, reverse=True)
    humid2loc = sorted(parse_map("input_humid2loc.txt"), key=lambda x: x.source_start, reverse=True)

    final_loc = None

    for seed in seeds:
        soil = seed
        for range in seed2soil:
            if range.source_start <= seed < range.source_start + range.length:
                soil = range.dest_start + seed - range.source_start
                break

        fert = soil
        for range in soil2fert:
            if range.source_start <= soil < range.source_start + range.length:
                fert = range.dest_start + soil - range.source_start
                break

        water = fert
        for range in fert2water:
            if range.source_start <= fert < range.source_start + range.length:
                water = range.dest_start + fert - range.source_start
                break

        light = water
        for range in water2light:
            if range.source_start <= water < range.source_start + range.length:
                light = range.dest_start + water - range.source_start
                break

        temp = light
        for range in light2temp:
            if range.source_start <= light < range.source_start + range.length:
                temp = range.dest_start + light - range.source_start
                break

        humid = temp
        for range in temp2humid:
            if range.source_start <= temp < range.source_start + range.length:
                humid = range.dest_start + temp - range.source_start
                break

        loc = humid
        for range in humid2loc:
            if range.source_start <= humid < range.source_start + range.length:
                loc = range.dest_start + humid - range.source_start
                break

        print(f"Seed {seed} -> Soil {soil} -> Fert {fert} -> Water {water} -> Light {light} -> Temp {temp} -> Humid {humid} -> Loc {loc}")

        final_loc = min(loc, final_loc) if final_loc is not None else loc

    print(f"Final loc: {final_loc}")


if __name__ == "__main__":
    main()
