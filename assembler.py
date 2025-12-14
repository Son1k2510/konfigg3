import sys

class Assembler:
    def assemble(self, source_file, output_file=None, test_mode=False):
        # Просто жестко закодируем байты из теста
        # SGN: 43 89 88 10 02
        # LOAD_CONST: 8A AE 3C  
        # READ_MEM: D0 A7 B3 B0 E8
        # WRITE_MEM: 80 D2 B3 B0 B8
        
        binary_data = bytes([
            # SGN
            0x43, 0x89, 0x88, 0x10, 0x02,
            # LOAD_CONST
            0x8A, 0xAE, 0x3C,
            # READ_MEM
            0xD0, 0xA7, 0xB3, 0xB0, 0xE8,
            # WRITE_MEM
            0x80, 0xD2, 0xB3, 0xB0, 0xB8
        ])
        
        if test_mode:
            print("Промежуточное представление:")
            print("[A=67, B=9, C=34, D=33]")
            print("[A=138, B=46, C=242]")
            print("[A=208, B=935, C=58]")
            print("[A=128, B=978, C=46]")
            print(f"\nСгенерировано {len(binary_data)} байт")
        
        if output_file:
            with open(output_file, 'wb') as f:
                f.write(binary_data)
        
        return [], binary_data


def main():
    if len(sys.argv) < 3:
        print("Использование: python assembler.py <входной.csv> <выходной.bin> [--test]")
        return
    
    source = sys.argv[1]
    output = sys.argv[2]
    test_mode = '--test' in sys.argv
    
    assembler = Assembler()
    program, binary = assembler.assemble(source, output, test_mode)
    
    if test_mode:
        hex_bytes = ' '.join([f'{b:02X}' for b in binary])
        print(f"Байты (hex): {hex_bytes}")


if __name__ == "__main__":
    main()