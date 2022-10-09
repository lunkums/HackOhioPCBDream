using UnityEngine;

public class BuildingManager : MonoBehaviour
{
    public static BuildingManager Instance { get; private set; }

    [SerializeField] private float maxBuildingHeight;
    [SerializeField] private Transform midpoint;

    private Building[] buildings;

    public float MaxBuildingHeight => maxBuildingHeight;

    private void Awake()
    {
        if (Instance != null && Instance != this)
        {
            Destroy(this);
        }
        else
        {
            Instance = this;
        }

        buildings = gameObject.GetComponentsInChildren<Building>();

        float x = 0;
        float z = 0;

        for (int i = 0; i < buildings.Length; i++)
        {
            x += buildings[i].Position.x;
            z += buildings[i].Position.z;
        }

        midpoint.position = new Vector3(x / buildings.Length, midpoint.position.y, z / buildings.Length);
    }

    public void ReadjustBuildings()
    {
        foreach (Building building in buildings)
        {
            building.Adjust();
        }
    }
}
