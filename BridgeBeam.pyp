<?xml version="1.0" encoding="utf-8"?>
<Element>
    <Script>
        <Name>BridgeBeam.py</Name>
        <Title>CreateBridgeBeam</Title>
        <Version>1.0</Version>
    </Script>

    <Page>
        <Name>Page3</Name>
        <Text>Polygon3D</Text>

        <Parameter>
            <Name>Color3</Name>
            <Text>Колір</Text>
            <Value>1</Value>
            <ValueType>Color</ValueType>
        </Parameter>
        <Parameter>
            <Name>Separator1</Name>
            <ValueType>Separator</ValueType>
        </Parameter>
        <Parameter>
            <Name>BeamLength</Name>
            <Text>Довжина балки (L)</Text>
            <Value>12000.</Value>
            <MinValue>12000.</MinValue>
            <ValueType>Length</ValueType>
        </Parameter>
        <Parameter>
            <Name>Separator2</Name>
            <ValueType>Separator</ValueType>
        </Parameter>
        <Parameter>
            <Name>TopShWidth</Name>
            <Text>Ширина верхньої полки (b1)</Text>
            <Value>600.</Value>
            <MinValue>600.</MinValue>
            <ValueType>Length</ValueType>
        </Parameter>
        <Parameter>
            <Name>BotShWidth</Name>
            <Text>Ширина нижньої полки (b2)</Text>
            <Value>480.</Value>
            <MinValue>480.</MinValue>
            <ValueType>Length</ValueType>
        </Parameter>
        <Parameter>
            <Name>RibThick</Name>
            <Text>Товщина ребра (b3)</Text>
            <Value>160.</Value>
            <MinValue>160.</MinValue>
            <ValueType>Length</ValueType>
        </Parameter>
        <Parameter>
            <Name>Separator3</Name>
            <ValueType>Separator</ValueType>
        </Parameter>
        <Parameter>
            <Name>BeamHeight</Name>
            <Text>Висота балки (H)</Text>
            <Value>1100.</Value>
            <MinValue>1100.</MinValue>
            <ValueType>Length</ValueType>
        </Parameter>
        <Parameter>
            <Name>BotShLowHeight</Name>
            <Text>Висота нижньої полки (h1)</Text>
            <Value>153.</Value>
            <MinValue>153.</MinValue>
            <ValueType>Length</ValueType>
        </Parameter>
        <Parameter>
            <Name>BotShUpHeight</Name>
            <Text>(h2)</Text>
            <Value>160.</Value>
            <MinValue>160.</MinValue>
            <ValueType>Length</ValueType>
        </Parameter>
        <Parameter>
            <Name>RibHeight</Name>
            <Text>Висота ребра (h3)</Text>
            <Value>467.</Value>
            <MinValue>467.</MinValue>
            <ValueType>Length</ValueType>
        </Parameter>
        <Parameter>
            <Name>TopShHeight</Name>
            <Text>Висота верхньої полки (h4)</Text>
            <Value>320.</Value>
            <MinValue>320.</MinValue>
            <ValueType>Length</ValueType>
        </Parameter>
        <Parameter>
            <Name>Separator4</Name>
            <ValueType>Separator</ValueType>
        </Parameter>
        <Parameter>
            <Name>HoleDepth</Name>
            <Text>Глибина до строповочного отвору (l5)</Text>
            <Value>350.</Value>
            <MinValue>350.</MinValue>
            <ValueType>Length</ValueType>
        </Parameter>
        <Parameter>
            <Name>HoleHeight</Name>
            <Text>Висота до строповочного отвору (h5)</Text>
            <Value>540.</Value>
            <ValueType>Length</ValueType>
        </Parameter>
        <Parameter>
            <Name>Separator5</Name>
            <ValueType>Separator</ValueType>
        </Parameter>
        <Parameter>
                <Name>RotationAngleX</Name>
                <Text>Поворот відносно осі X</Text>
                <Value>0</Value>
                <ValueType>Angle</ValueType>
            </Parameter>
            <Parameter>
                <Name>RotationAngleY</Name>
                <Text>Поворот відносно осі Y</Text>
                <Value>0</Value>
                <ValueType>Angle</ValueType>
            </Parameter>
            <Parameter>
                <Name>RotationAngleZ</Name>
                <Text>Поворот відносно осі Z</Text>
                <Value>0</Value>
                <ValueType>Angle</ValueType>
            </Parameter>
    </Page>    
</Element>
