class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        current=bank[0].count("1")
        beams=0
        for floor in bank[1:]:
            devices=floor.count("1")
            print(devices)
            if devices==0:
                continue
            beams+=(devices*current)
            current=devices
        return beams

        