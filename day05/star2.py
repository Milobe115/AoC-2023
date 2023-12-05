from dataclasses import dataclass


@dataclass
class RangeMap:
    source_start: int
    dest_start: int
    length: int

    def __init__(self, source_start: int, dest_start: int, length: int):
        self.source_start = source_start
        self.dest_start = dest_start
        self.length = length


@dataclass
class Range:
    start: int
    end: int

    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end


def parse_map(path: str):
    with open(path, "r") as f:
        lines = f.read().splitlines()

    range_map: list[RangeMap] = []
    for line in lines:
        dst_start, src_start, length = line.split(" ")
        range_map.append(RangeMap(int(src_start), int(dst_start), int(length)))

    return range_map


def main():
    with open("input_seeds.txt", "r") as f:
        seed_ranges = [int(seed) for seed in f.read().split(" ")]

    seed2soil = sorted(parse_map("input_seed2soil.txt"), key=lambda x: x.source_start)
    soil2fert = sorted(parse_map("input_soil2fert.txt"), key=lambda x: x.source_start)
    fert2water = sorted(parse_map("input_fert2water.txt"), key=lambda x: x.source_start)
    water2light = sorted(parse_map("input_water2light.txt"), key=lambda x: x.source_start)
    light2temp = sorted(parse_map("input_light2temp.txt"), key=lambda x: x.source_start)
    temp2humid = sorted(parse_map("input_temp2humid.txt"), key=lambda x: x.source_start)
    humid2loc = sorted(parse_map("input_humid2loc.txt"), key=lambda x: x.source_start)

    final_loc = None

    seeds = []
    for i in range(0, len(seed_ranges), 2):
        seeds.append(Range(seed_ranges[i], seed_ranges[i] + seed_ranges[i + 1]))

    soils = []
    for seed in seeds:
        for _seed2soil in seed2soil:
            if _seed2soil.source_start <= seed.start < _seed2soil.source_start + _seed2soil.length and seed.start < seed.end:
                soil_range_start = seed.start - _seed2soil.source_start + _seed2soil.dest_start
                soil_range_end = min(_seed2soil.dest_start + _seed2soil.length,
                                     seed.end - _seed2soil.source_start + _seed2soil.dest_start)
                if soil_range_start < soil_range_end:
                    soils.append(Range(soil_range_start, soil_range_end))
                    seed.start = _seed2soil.source_start + _seed2soil.length
        if seed.start < seed.end:
            soils.append(Range(seed.start, seed.end))

    ferts = []
    for soil in soils:
        for _soil2fert in soil2fert:
            if _soil2fert.source_start <= soil.start < _soil2fert.source_start + _soil2fert.length and soil.start < soil.end:
                fert_range_start = soil.start - _soil2fert.source_start + _soil2fert.dest_start
                fert_range_end = min(_soil2fert.dest_start + _soil2fert.length,
                                     soil.end - _soil2fert.source_start + _soil2fert.dest_start)
                if fert_range_start < fert_range_end:
                    ferts.append(Range(fert_range_start, fert_range_end))
                    soil.start = _soil2fert.source_start + _soil2fert.length
        if soil.start < soil.end:
            ferts.append(Range(soil.start, soil.end))

    waters = []
    for fert in ferts:
        for _fert2water in fert2water:
            if _fert2water.source_start <= fert.start < _fert2water.source_start + _fert2water.length and fert.start < fert.end:
                water_range_start = fert.start - _fert2water.source_start + _fert2water.dest_start
                water_range_end = min(_fert2water.dest_start + _fert2water.length,
                                      fert.end - _fert2water.source_start + _fert2water.dest_start)
                if water_range_start < water_range_end:
                    waters.append(Range(water_range_start, water_range_end))
                    fert.start = _fert2water.source_start + _fert2water.length
        if fert.start < fert.end:
            waters.append(Range(fert.start, fert.end))

    lights = []
    for water in waters:
        for _water2light in water2light:
            if _water2light.source_start <= water.start < _water2light.source_start + _water2light.length and water.start < water.end:
                light_range_start = water.start - _water2light.source_start + _water2light.dest_start
                light_range_end = min(_water2light.dest_start + _water2light.length,
                                      water.end - _water2light.source_start + _water2light.dest_start)
                if light_range_start < light_range_end:
                    lights.append(Range(light_range_start, light_range_end))
                    water.start = _water2light.source_start + _water2light.length
        if water.start < water.end:
            lights.append(Range(water.start, water.end))

    temps = []
    for light in lights:
        for _light2temp in light2temp:
            if _light2temp.source_start <= light.start < _light2temp.source_start + _light2temp.length and light.start < light.end:
                temp_range_start = light.start - _light2temp.source_start + _light2temp.dest_start
                temp_range_end = min(_light2temp.dest_start + _light2temp.length,
                                     light.end - _light2temp.source_start + _light2temp.dest_start)
                if temp_range_start < temp_range_end:
                    temps.append(Range(temp_range_start, temp_range_end))
                    light.start = _light2temp.source_start + _light2temp.length
        if light.start < light.end:
            temps.append(Range(light.start, light.end))

    humids = []
    for temp in temps:
        for _temp2humid in temp2humid:
            if _temp2humid.source_start <= temp.start < _temp2humid.source_start + _temp2humid.length and temp.start < temp.end:
                humid_range_start = temp.start - _temp2humid.source_start + _temp2humid.dest_start
                humid_range_end = min(_temp2humid.dest_start + _temp2humid.length,
                                      temp.end - _temp2humid.source_start + _temp2humid.dest_start)
                if humid_range_start < humid_range_end:
                    humids.append(Range(humid_range_start, humid_range_end))
                    temp.start = _temp2humid.source_start + _temp2humid.length
        if temp.start < temp.end:
            humids.append(Range(temp.start, temp.end))

    locs = []
    for humid in humids:
        for _humid2loc in humid2loc:
            if _humid2loc.source_start <= humid.start < _humid2loc.source_start + _humid2loc.length and humid.start < humid.end:
                loc_range_start = humid.start - _humid2loc.source_start + _humid2loc.dest_start
                loc_range_end = min(_humid2loc.dest_start + _humid2loc.length,
                                    humid.end - _humid2loc.source_start + _humid2loc.dest_start)
                if loc_range_start < loc_range_end:
                    locs.append(Range(loc_range_start, loc_range_end))
                    humid.start = _humid2loc.source_start + _humid2loc.length
        if humid.start < humid.end:
            locs.append(Range(humid.start, humid.end))

    final_loc = min(x.start for x in locs)

    print(f"Final loc: {final_loc}")

    # 37384986


if __name__ == "__main__":
    main()
